from .schemas import GetResume
from ml.text_preprocessing import PrepTransformer
from ml.text_work import text_work

def read_all_resume(body: GetResume):

    resume_params = body.dict(exclude_none=True)

    work_flow = [param['text'] for param in resume_params['content']]

    work_flow.append(resume_params['requirements']) 

    PrepTransform = PrepTransformer()

    work_flow = [PrepTransform.transform(text) for text in work_flow]

    return text_work(work_flow)
