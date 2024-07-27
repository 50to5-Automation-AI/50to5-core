import requests
from autogen import GroupChatManager

class QualityControlAgent(GroupChatManager):
    ...

    def send_slack_notification(self, message: str):
        payload = {
            "text": message
        }
        response = requests.post(self.slack_config["webhook_url"], json=payload)
        self.logger.info(f"Slack message sent: {response.status_code}")

    def report_feedback(self):
        summary = self.generate_feedback_summary()
        self.send_slack_notification(
            message=f"Quality Control Feedback: {summary}"
        )

    def generate_feedback_summary(self):
        # Logic to generate feedback summary
        return "Details of the quality control feedback..."
