from robusta.api import *


@action
def delete_pod(event: PodEvent):
    """
    Deletes a pod
    """
    if not event.get_pod():
        logging.info("Failed to get the pod for deletion")
        event.add_enrichment(
            [
                MarkdownBlock(
                    "*Alert Explanation:* Robusta FAILED to delete faulty POD, please action manually."

                ),
            ],
            annotations={SlackAnnotations.UNFURL: False},
        )
        return

    event.get_pod().delete()

    event.add_enrichment(
        [
            MarkdownBlock(
                "*Alert Explanation:* The faulty pod has now been deleted by Robusta"

            ),
        ],
        annotations={SlackAnnotations.UNFURL: False},
    )
