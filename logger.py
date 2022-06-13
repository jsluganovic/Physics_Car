
import logging
class LoggerDemoConsole:
   def testLog(self):
       #logger = logging.getLogger('demologger')
       logger = logging.getLogger(LoggerDemoConsole.__name__)
       logger.setLevel(logging.INFO)
       fileHandler = logging.FileHandler("demo.log",mode='a')
       fileHandler.setLevel(logging.INFO)
       formatter = logging.Formatter('%(asctime)s - %(name)s%(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S%p')
       fileHandler.setFormatter(formatter)
       logger.addHandler(fileHandler)
       logger.debug('debug message')
       logger.info('info message')
       logger.warning('warn message')
       logger.error('error message')
       logger.critical('critical message')
demo = LoggerDemoConsole()
demo.testLog()
print("Done")