class BaseModel:
    PK = 1
    TYPE = 'Basic Model'

    def __init__(self, data_type, title, content, created_at, updated_at):
        self.PK = BaseModel.PK
        self.data_type = data_type 
        self.title = title 
        self.content = content 
        self.created_at = created_at 
        self.updated_at = updated_at
        BaseModel.PK += 1
    
    def save(self):
        print('데이터를 저장합니다.')

class Novel(BaseModel):
    # author을 추가했는데 이거를 basemodel에서도 사용할 수있는건가?
    def __init__(self, data_type, title, content, created_at, updated_at, author):
        super().__init__(data_type, title, content, created_at, updated_at)
        self.author = author
    
class Other(BaseModel):
    TYPE = 'OtherModel'
    
    # basemodel클래스의 save메서드 호출할 필요가 있나 ? 형식이 똑같은데???
    def save(self):
        # 이렇게만 해도 상속이되는데 super 사용하는 이유- 1?
        print('데이터를 다른 장소에 저장합니다.')

class ExtendedModel(Novel, Other):
    TYPE = 'Extended Type' 

    def display_info(self):
        # 이렇게만 해도 상속이되는데 super 사용하는 이유- 2?
        print('ExtendedModel 인스턴스의 정보 출력 및 저장 메서드 호출')
        # 왜 TYPE를 Other.TYPE로 하면 안되지?, self.type로 하면 의존성이 높아진다?
        print(f'PK: {self.PK}, TYPE: {Other.TYPE}, Extended Type: {self.TYPE}')
        
    def save(self):
        print('데이터를 확장해서 저장합니다.')
    
    

extended_instance = ExtendedModel('소설', '홍길동', '고전 소설', 1618, 1692, '허균')
extended_instance.display_info()
extended_instance.save()