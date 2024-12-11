import grpc
import sum_pb2
import sum_pb2_grpc

def run():
    # Establecer conexión con el servidor RPC
    channel = grpc.insecure_channel('localhost:50051')
    stub = sum_pb2_grpc.SumServiceStub(channel)

    # Crear una solicitud de suma
    request = sum_pb2.SumRequest(a=5, b=3)

    # Hacer la llamada RPC y obtener la respuesta
    response = stub.Add(request)

    print(f"Resultado de la suma: {response.result}")

if __name__ == '__main__':
    run()
