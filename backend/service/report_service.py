from backend.dao.report_dao import ReportDAO
class ReportService:
    @staticmethod
    def dashboard(): return ReportDAO.dashboard()
    @staticmethod
    def funnel(): return ReportDAO.recruitment_funnel()
    @staticmethod
    def pending_interviews(): return ReportDAO.pending_interviews()
    @staticmethod
    def company_placements(): return ReportDAO.company_placements()
