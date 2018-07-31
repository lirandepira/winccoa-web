class WinCCRouter:
    """
    A router to control all read database operations on models in the api application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read winccoa models go to winccoa_db.
        """
        if model._meta.app_label == 'winccoa':
            return 'winccoa_db'
        return None
