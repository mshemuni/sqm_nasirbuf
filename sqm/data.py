import serial
from logging import getLogger

import numpy as np

from . import ast


class Handle:
    def __init__(self, port, logger=None):
        self.port = port
        self.logger = logger or getLogger('dummy')
        self.con = None
        self.ast_sqm = ast.SQM(logger=self.logger)
        self.ast_time = ast.Time(logger=self.logger)

    def connect(self):
        self.logger.info(f'Creating a connection on {self.port}')
        try:
            self.con = serial.Serial(port=self.port, baudrate=115200,
                                     parity=serial.PARITY_NONE,
                                     stopbits=serial.STOPBITS_ONE,
                                     bytesize=serial.EIGHTBITS, timeout=1)
        except Exception as e:
            self.logger.error(e)

    def close(self):
        self.logger.info(f'Closing the connection on {self.port}')
        try:
            if self.con is not None:
                self.con.close()
        except Exception as e:
            self.logger.error(e)

    def __read__(self):
        self.logger.info(f'Reading a value from {self.port}')
        try:
            self.con.write(str.encode("rx\n"))
            self.con.flush()
            tmp = str(self.con.readline()).split()
            raw_mag = float(tmp[1].split(",")[0].replace("m", ""))
            tempe = float(tmp[2].split("C")[0])
            new_mag = self.ast_sqm.mag(raw_mag)
            flux = self.ast_sqm.flux(raw_mag)
            jd = self.ast_time.jd(self.ast_time.now())
            return np.array([jd, raw_mag, tempe, new_mag, flux])
        except Exception as e:
            self.logger.error(e)

    def read(self):
        self.logger.info(f"Reading from {self.port}")
        try:
            self.connect()
            data = self.__read__()
            self.close()
            return np.array(data)
        except Exception as e:
            self.logger.error(e)
            self.close()

    def multi_read(self, n=100):
        self.logger.info(f"Reading {n} values from {self.port}")
        try:
            d = []
            self.connect()
            for _ in range(n):
                d.append(np.array(self.__read__()))
            self.close()
            return np.array(d)
        except Exception as e:
            self.logger.error(e)
            self.close()

    def stat_read(self, n=100):
        self.logger.info(f"Statistics from {n} values")
        try:
            data = self.multi_read(n=n)
            return np.mean(data, axis=0)
        except Exception as e:
            self.logger.error(e)
            self.close()
