from datetime import datetime

class Log_class:
    """Logging Class
    """

    def __init__(self, folder_path, file_name):
        self.folder_path = folder_path
        self.file_name = file_name

    def InfoLog(self, log_message):
        """
            Description: This is for creating log.
            Method: Create_log_file
            Input: log_message
            Output: Save log_message in file
            On error: Raise error message
        """
        try:
            now = datetime.now()
            date = now.date()
            current_time = now.strftime("%H:%M:%S")

            with open(self.folder_path + self.file_name, 'a') as file:
                file.write(str(date) + "\t" + str(current_time) + "\t\t" + "INFO" + "\t\t" + log_message + "\n")
        except Exception as e:
            raise e
            
            
    def ErrorLog(self, log_message):
        """
            Description: This is for creating log.
            Method: Create_log_file
            Input: log_message
            Output: Save log_message in file
            On error: Raise error message
        """
        try:
            now = datetime.now()
            date = now.date()
            current_time = now.strftime("%H:%M:%S")

            with open(self.folder_path + self.file_name, 'a') as file:
                file.write(str(date) + "\t" + str(current_time) + "\t\t" + "ERROR" + "\t\t" +  + log_message + "\n")
        except Exception as e:
            raise e