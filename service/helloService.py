from src.hello.repo.helloRepo import helloRepo

class HelloService:
    def sayHello(self):
        return helloRepo.sayHello()

helloService = HelloService()