def download_input():
    """Downloads a video or audio file from GCS Bucket"""
    pass


def validate_format():
    """Validate the file format of the provided file.

    Accepted formats: 
        Audio:
        - MP3 (.mp3)
        - WAV (.wav)
        - FLAC (.flac)
        - WMA (.wma)
        - M4A (.m4a)

        Video:
        - MP4 (.mp4)
        - AVI (.avi)
        - MOV (.mov)
        - MKV (.mkv)
        - FLV (.flv)
    """
    pass


def check_temp_custom_dir():
    """Checks if the directory doens't exist before creating it"""
    pass


def create_custom_output_dir():
    """Creates output directory"""
    pass


def exec_whisper():
    """Executes command on terminal with the provided files and directories"""
    pass


def test_generated_files():
    """Checks if all files get created (5)
    And returns true otherwise returns false
    """
    pass


def test_files_not_empty():
    """Checks if file content is not empty"""
    pass


def compress_output_dir():
    """Compress output dir into .zip"""
    pass


def move_to_upload_path():
    """Moves from stage path to upload path."""
    pass