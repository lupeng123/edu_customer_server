
from langchain_core.tools import tool
from rag.rag_service import RagService

rag_service = RagService()

@tool
def rag_summarize(query:str) -> str:
    """从向量数据库中检索参考资料"""
    return rag_service.rag_summarize(query)

@tool
def query_student_order(phone: str):
    """根据家长手机号，查询学员报名订单、科目、班次、开课时间"""
    return "订单信息：春季语文培优B班，2026-03-07开课，每周日14:30-16:00，实付1800元"

@tool
def query_remaining_course(student_id: str):
    """根据学员id，查询剩余课时、最近上课记录"""
    return "剩余课时：12节，最近上课记录：2026-10-20 语文培优课"

@tool
def submit_change_class(student_id: str, target_class: str, reason: str):
    """提交调班工单，参数：学员id、目标班次名称、调班原因"""
    return "调班工单已提交，教务1个工作日内审核，结果短信通知"

@tool
def transfer_to_human(reason: str):
    """转人工客服，参数：转接原因"""
    return "已经为您转接人工客服，请您耐心等待，助教很快会联系您"

tools = [rag_summarize,query_student_order, query_remaining_course, submit_change_class, transfer_to_human]