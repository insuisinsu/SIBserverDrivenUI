# api/schema.py
# GraphQL에서 MongoDB와 연동된 일종의 테이블(Schema)를 정의하는 파일

import graphene

# Model 과 ObjectType 가져오기
# Model은 실제 MongoDB를 조작할 때 사용
# ObjectType은 반환값에 대한 타입을 지정할 때 사용
from api.models import RankModel, RankType

# Query 설정
# Query는 데이터를 조회하는데 사용되며, 각 필드는 데이터의 집합임
class Query(graphene.ObjectType):
    # 데이터의 집합을 정의
    # graphene.Field는 한 개의 결과를 반환
    # graphene.List는 여러개의 결과를 반환
    # 각 함수의 첫번째 인자는 결과값에 대한 ObjectType임
    # 각 인자는 Resolver로 전달됨

    # 모든 랭킹 목록
    ranks = graphene.List(RankType)

    # 특정 모드에 대한 랭킹 목록
    ranks_for_mode = graphene.List(RankType, mode=graphene.String(required=True))

    # 특정 랭킹에 대한 정보
    rank = graphene.Field(RankType, id=graphene.String(required=True))

    # 각 Field에 대한 Resolver 설정
    # Resolver는 조회 결과에 대한 상세 구현함
    # MongoDB에서 모든 랭킹 목록을 조회
    def resolve_ranks(parent, info):
        return RankModel.objects.all()
    
    # MongoDB에서 특정 모드의 모든 랭킹 목록을 조회
    def resolve_ranks_for_mode(parent, info, mode):
        return RankModel.objects(mode=mode).all()
    
    # MongoDB에서 특정 랭킹을 조회
    def resolve_rank(parent, info, id):
        return RankModel.objects.get(id=id)

# Schema 생성
# Schema는 GraphQL의 전체 데이터 구조를 의미함
# ObjectType, Query, Mutation 등을 포괄함
schema = graphene.Schema(
    query=Query,
    types=[
        RankType
    ]
)