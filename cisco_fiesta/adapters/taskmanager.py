from apscheduler.schedulers.blocking import BlockingScheduler
import mail_adapter


def job_schedule():
    instance = mail_adapter.MailScrapper()
    raw = mail_adapter.MailScrapper.find_mail(instance)
    mail_adapter.MailScrapper.get_attachments(instance,raw)
    
            


scheduler = BlockingScheduler({'apscheduler.timezone': 'Brazil/East'})

scheduler.add_job(job_schedule, 'cron', hour='*', minute=51)
scheduler.start()
