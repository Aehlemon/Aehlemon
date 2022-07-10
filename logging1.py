import logging

logger = logging.getLogger("main") # logger 선언
stream_handler = logging.StreamHandler() # logger의 output 방법 선언
logger.addHandler(stream_handler) # logger의 output 등록

logger.setLevel(logging.DEBUG) # 상태별로 logging. 다르게 불러올 수 있음
logger.debug("틀렸습니다.")
logger.info("확인하세요")
logger.warning("조심해")
logger.error("에러!!")
logger.critical("망..")

# 틀렸습니다.
# 확인하세요
# 조심해
# 에러!!
# 망..

logger.setLevel(logging.CRITICAL) # 상태별로 logging. 다르게 불러올 수 있음
logger.debug("틀렸습니다.")
logger.info("확인하세요")
logger.warning("조심해")
logger.error("에러!!")
logger.critical("망..")

# 망..