from django.db import models
from django.urls import reverse
# get_absolute_url 방법을 쓸때 모델에다 정의 할때는 reverse 메소드,, 클레스 뷰에서 필드값으로 정의할때는 reverse_lazy 메서드

# Create your models here.
# 모델 : 데이터베이스를 sql 없이 다루려고 모델을 사용
# 데이터를 객체화 해서 다루겠다.
# 모델 : 테이블
# 모델의 필드 : 테이블의 컬럼(열)
# 인스턴스 = 테이블의 레코드(행)
# 필드값 : 레코드의 컬럼 데이터값

class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site Url')
    # 필드의 종류가 결정하는 것
    # 1. 데이터베이스의 컬럼 종류
    # 2. 제약 사항(몇글자까지, 한글만 ? )
    # 3. form의 종류 결정
    # 4. form 제약사항

    def __str__(self):
        return f"이름 : {self.site_name}, 주소 : {self.url}"

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])


# 모델을 만들었다. => 데이터베이스에 어떤 데이터들을 어떤 형태로 넣을지 결정!
# 마이그레이션(migration) => 데이터베이스에 모델의 내용을 반영(테이블 수정)
# makemigrations => 모델의 변경사항을 추적해서 기록
# 모델 수정, 추가하고 마이그레이션 필수