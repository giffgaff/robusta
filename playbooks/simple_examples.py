from robusta.api import *


@action
def test_pod_orm(event: PodEvent):
    logging.info("running test_pod_orm")
    pod = event.obj

    images = [container.image for container in event.obj.spec.containers]
    logging.info(f"pod images are {images}")

    exec_resp = pod.exec("ls -l /")
    logging.info(f"pod ls / command: {exec_resp}")

    logging.info(f"deleting pod {pod.metadata.name}")
    RobustaPod.deleteNamespacedPod(pod.metadata.name, pod.metadata.namespace)
    logging.info(f"pod deleted")


class EchoParams(BaseModel):
    message: str


@action
def echo(event: ExecutionBaseEvent, params: EchoParams):
    logging.warning(f"echo: {params.message}")
