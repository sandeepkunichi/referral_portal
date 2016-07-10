from django.forms import ModelChoiceField


class JobPostingModelChoiceField(ModelChoiceField):
    def label_from_instance(self, job_posting):
        return job_posting.title
