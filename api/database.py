# api/database.py
# MongoDB 연결 및 기초 데이터 세팅 파일

from mongoengine import connect
from api.models import RankModel

# 실제 MongoDB의 주소와 Database를 입력해야함
MONGO_DTATBASE="graphql-example"
MONGO_HOST="mongomock://localhost"

# Database 연결
# MongoDB 연결
conn = connect(MONGO_DTATBASE, host=MONGO_HOST, alias="default")

# 기초 데이터 Insert 함수
# 임의의 기초 데이터 입력
# save() 함수는 mongoengine에서 제공하는 insert 기능
def init_db():
    rank = RankModel(name="kim", mode="3x3", score=2, isMobile=False, reg_dttm="20200413170848")
    rank.save() # Insert
    
    rank = RankModel(name="choi", mode="3x3", score=128, isMobile=False, reg_dttm="20200413170848")
    rank.save() # Insert
    
    rank = RankModel(name="lee", mode="4x4", score=1024, isMobile=False, reg_dttm="20200413170848")
    rank.save() # Insert
    
    rank = RankModel(name="heo", mode="4x4", score=16, isMobile=False, reg_dttm="20200413170848")
    rank.save() # Insert