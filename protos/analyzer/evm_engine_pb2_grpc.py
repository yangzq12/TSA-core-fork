# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from protos.analyzer import bytecode_analyzer_pb2 as protos_dot_analyzer_dot_bytecode__analyzer__pb2


class EVMEngineStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AnalyseByteCode = channel.unary_unary(
                '/analyzer.EVMEngine/AnalyseByteCode',
                request_serializer=protos_dot_analyzer_dot_bytecode__analyzer__pb2.ByteCodeAnalysisRequest.SerializeToString,
                response_deserializer=protos_dot_analyzer_dot_bytecode__analyzer__pb2.ByteCodeAnalysisResponse.FromString,
                )


class EVMEngineServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AnalyseByteCode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EVMEngineServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AnalyseByteCode': grpc.unary_unary_rpc_method_handler(
                    servicer.AnalyseByteCode,
                    request_deserializer=protos_dot_analyzer_dot_bytecode__analyzer__pb2.ByteCodeAnalysisRequest.FromString,
                    response_serializer=protos_dot_analyzer_dot_bytecode__analyzer__pb2.ByteCodeAnalysisResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'analyzer.EVMEngine', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class EVMEngine(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AnalyseByteCode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/analyzer.EVMEngine/AnalyseByteCode',
            protos_dot_analyzer_dot_bytecode__analyzer__pb2.ByteCodeAnalysisRequest.SerializeToString,
            protos_dot_analyzer_dot_bytecode__analyzer__pb2.ByteCodeAnalysisResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
