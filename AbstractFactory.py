class UniversityFactory:
    def get_university_type(self, score):
        if score > 100:
            return PublicUniversity()
        else:
            return PrivateUniversity()


class PublicUniversity:
    def get_university(self, subject):
        if subject == 'math':
            return MIT()
        elif subject == "physics":
            return IIT()
        else:
            return AIIMS()


class MIT:
    def __init__(self):
        self.name = 'MIT'


class IIT:
    def __init__(self):
        self.name = 'IIT'


class AIIMS:
    def __init__(self):
        self.name = 'AIIMS'


class PrivateUniversity:
    def get_university(self, subject):
        if subject == 'math':
            return LPU()
        elif subject == "physics":
            return Amity()
        else:
            return DAV()


class LPU:
    def __init__(self):
        self.name = 'LPU'


class Amity:
    def __init__(self):
        self.name = 'Amity'


class DAV:
    def __init__(self):
        self.name = 'DAV'


# Usage example:

university_factory = UniversityFactory()

# Test for a Public University with score > 100
public_university = university_factory.get_university_type(102)
print(public_university.get_university('math').name)  # MIT

# Test for a Private University with score <= 100
private_university = university_factory.get_university_type(92)
print(private_university.get_university('math').name)  # LPU
