class UrlBuilder:
    def __init__(self , builder):
        self.protocol = builder.protocol
        self.domain = builder.domain
        self.port = builder.port

    def _print(self):
        print(f"Protocol: {self.protocol}")
        print(f"Domain: {self.domain}")
        print(f"Port: {self.port}")

    class Builder:
        def __init__(self):
            self.protocol = None
            self.domain = None
            self.port = None

        def with_protocol(self, protocol):
            self.protocol = protocol
            return self

        def with_domain(self, domain):
            self.domain = domain
            return self

        def with_port(self, port):
            self.port = port
            return self

        def build(self):
            return UrlBuilder(self)

# Example Usage:
builder_ = UrlBuilder.Builder()
builder_.with_port(1000)
x = builder_.build()
x._print()