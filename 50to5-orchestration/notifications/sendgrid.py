import sendgrid
from sendgrid.helpers.mail import Mail

class InitializationAgent(AssistantAgent):
    ...
    
    def send_email_notification(self, subject: str, content: str):
        sg = sendgrid.SendGridAPIClient(api_key=self.sendgrid_config["api_key"])
        email = Mail(
            from_email=self.sendgrid_config["from_email"],
            to_emails=self.sendgrid_config["to_email"],
            subject=subject,
            html_content=content
        )
        response = sg.send(email)
        self.logger.info(f"Email sent: {response.status_code}")

    def report_end_of_chat(self):
        summary = self.generate_summary()
        self.send_email_notification(
            subject=f"Chat Session {self.session_id} Summary",
            content=summary
        )

    def generate_summary(self):
        # Logic to generate chat summary
        return "<h1>Chat Summary</h1><p>Details of the chat session...</p>"