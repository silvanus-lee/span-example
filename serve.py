from concurrent.futures import ThreadPoolExecutor
import time
import logging
import pickle
import os

import grpc
from sklearn.linear_model import ElasticNet

import serve_pb2
import serve_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


# for demo only
os.environ["SPAN_MODEL_PATH"] = "model.pickle"


class WineQualityService(serve_pb2_grpc.WineQualityPredictorServicer):
    def __init__(self):
        with open(os.environ["SPAN_MODEL_PATH"], "rb") as model_file:
            self.model: ElasticNet = pickle.load(model_file)

    def PredictQuality(self, request, context):
        return serve_pb2.PredictResponse(
            quality=self.model.predict(
                [
                    (
                        request.fixed_acidity,
                        request.volatile_acidity,
                        request.citric_acid,
                        request.residual_sugar,
                        request.chlorides,
                        request.free_sulfur_dioxide,
                        request.total_sulfur_dioxide,
                        request.density,
                        request.ph,
                        request.sulphates,
                        request.alcohol,
                    )
                ]
            )
        )


def serve():
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    serve_pb2_grpc.add_WineQualityPredictorServicer_to_server(
        WineQualityService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    logging.basicConfig()
    serve()
