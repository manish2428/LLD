#Following is an example of mailing/messaging services and how to trigger it
from abc import  ABC, abstractmethod
class Notification(ABC):
    @abstractmethod
    def trigger(self):
        pass

    @abstractmethod
    def create_template(self):
        pass

    @abstractmethod
    def modify_template(self):
        pass


class MalingService(Notification):
    def trigger(self):
        print("Mail is being triggered")

    def create_template(self):
        print("Creating a template")

    def modify_template(self):
        print("Modifying a template")


class SMSService(Notification):
    def trigger(self):
        print("SMS has been triggered")

    def create_template(self):
        print("Creating a template")

    def modify_template(self):
        print("Modifying a template")


class AbstractNotification(ABC):
    @abstractmethod
    def perform_operation(self):
        pass


class AbstractMailingService(AbstractNotification):
    def perform_operation(self):
        return MalingService()
    
class AbstractSMSService(AbstractNotification):
    def perform_operation(self):
        return SMSService()
    

def send_notification(service : AbstractNotification):
    return service.perform_operation()

# send_mail = AbstractMailingService()
# send_sms = AbstractSMSService()

send_mail = send_notification(AbstractMailingService())
send_sms = send_notification(AbstractSMSService())
#sending sms
send_sms.create_template()
send_sms.trigger()

#sending mail
send_mail.create_template()
send_mail.trigger()
