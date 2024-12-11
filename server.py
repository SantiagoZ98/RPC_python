import grpc
from concurrent import futures
import time

# Importar los archivos generados por protoc
import sum_pb2
import sum_pb2_grpc

# Implementar el servicio de suma
class SumService(sum_pb2_grpc.SumServiceServicer):
    def Add(self, request, context):
        result = request.a + request.b
        return sum_pb2.SumResponse(result=result)

# Configurar y arrancar el servidor
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sum_pb2_grpc.add_SumServiceServicer_to_server(SumService(), server)
    server.add_insecure_port('[::]:50051')
    print("Servidor RPC escuchando en puerto 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
