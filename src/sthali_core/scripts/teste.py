class Base:
    def __init__(self, *args, **kwargs) -> None:
        print("Base.__init__")
        super().__init__(*args, **kwargs)


    def __init_subclass__(cls, *args, **kwargs) -> None:
        print("Base.__init_subclass__")


class A:
    def __init__(self, *args, **kwargs):
        print("A.__init__")
        super().__init__(*args, **kwargs)

    def __init_subclass__(cls, *args, **kwargs) -> None:
        print("A.__init_subclass__")


class B(Base):
    def __init__(self, *args, **kwargs):
        print("B.__init__")
        super().__init__(*args, **kwargs)

    def __init_subclass__(cls, *args, **kwargs) -> None:
        print("B.__init_subclass__")


class C(B):
    def __init__(self, *args, **kwargs):
        print("C.__init__")
        super().__init__(*args, **kwargs)

    def __init_subclass__(cls, a, *args, **kwargs) -> None:
        print("C.__init_subclass__")
        cls.a = a


class D(C, a="teste"):
    def __init__(self, *args, **kwargs):
        print("D.__init__")
        super().__init__(*args, **kwargs)

    def __init_subclass__(cls, *args, **kwargs) -> None:
        print("D.__init_subclass__")


if __name__ == "__main__":
    breakpoint()
    x = 1
