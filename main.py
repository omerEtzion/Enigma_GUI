from py4j.java_gateway import JavaGateway, GatewayParameters

if __name__ == '__main__':

    gateWay = JavaGateway(25333)
    enigma = gateWay.entry_point.getEnigma()
    print(enigma.getInt())
