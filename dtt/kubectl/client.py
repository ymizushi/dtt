from kubernetes import client, config
from kubernetes.client.rest import ApiException as OrigApiException

class Client:
    @classmethod
    def load_config(cls):
        config.load_kube_config()

    def __init__(self):
        self._v1 = client.CoreV1Api()

    def list_namespaced_pod(self, namespace, watch=False):
        return self._v1.list_namespaced_pod(namespace, watch=False)

    def list_pod_for_all_namespaces(self, watch=False):
        return self._v1.list_pod_for_all_namespaces(watch=False)
