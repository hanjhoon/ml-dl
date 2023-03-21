# [HTTP 통신](https://wildeveloperetrain.tistory.com/37)

## http/https
> 서버와 클라이언트가 인터넷 상에서 데이터를 주고 받기 위한 프로토콜(약속)이다.

## [URL 구조](https://developer.mozilla.org/ko/docs/Web/HTTP/Basics_of_HTTP/Identifying_resources_on_the_Web)
> https://news.naver.com:443/main/main.naver?mode=LSD&mid=shm&sid1=100
- 프로토콜: https
> 프로토콜은 컴퓨터끼리 네트워크 통신을 할 때 규격이다. HTTP, HTTPS, SMTP(이메일), SSH(원격 통신) 등이 있다.
- 호스트 주소: news.naver.com
> 호스트 주소는 도메인 네임 또는 IP 주소이다. 즉, 서버(서버 컴퓨터)의 고유 주소를 표시하는 영역이다.  
> 도에인은 식별하기 어려운 IP 주소를 쉽게 이해할 수 있는 문자로 표시한 주소이다.
- 포트 번호: 443
> 서버(서버 컴퓨터)에서 네트워크 서비스나 특정 프로세스를 식별하는 논리 단위이다.    
> - http는 80 포트  
> - https는 443 포트   
- 경로: main/main.naver
> 서버(서버 컴퓨터)에서 서비스 별로 정의한 주소 경로이다.
- 쿼리: mode=LSD&mid=shm&sid1=100
> `?`를 기점으로 `key=value` 형태로 데이터를 표현하며, 서버(서버 컴퓨터)에 특정 요청을 할 때 사용한다.

## [HTTP 응답 상태코드](https://developer.mozilla.org/ko/docs/Web/HTTP/Status)
> 클라이언트가 서버에 요청을 하면, 서버는 요청에 대한 처리 상태를 숫자로 반환하는데 이를 응답코드라고 합니다.
- 100 ~ 109: 메시지 정보
- 200 ~ 206: 요청 성공
> 예) 200: OK(요청 성공)
- 300 ~ 305: 리다이렉션
- 400 ~ 415: 클라이언트 에러
> 예) 404: Not Found(요청 리소스를 찾을 수 없음)
- 500 ~ 505: 서버에러
> 예) 500: Internal Server Error(서버 문제로 오류 발생)

## [HTTP Method](https://developer.mozilla.org/ko/docs/Web/HTTP/Methods)
> 클라이언트가 서버에 요청하는 방법
- GET: 보통 리소스를 조회할 때 사용하며, 서버에 전달하고 싶은 데이터는 query를 통해서 전달한다. 
- POST: 데이터 요청을 처리하고, 메시지 바디를 통해 서버로 데이터를 전달한다. 

## [HTTP Header](https://developer.mozilla.org/ko/docs/Web/HTTP/Headers)
- User-Agent



