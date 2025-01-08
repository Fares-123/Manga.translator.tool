import subprocess
import os

def start_xmrig(wallet_address, pool_url, cpu_threads=2):
    """
    تشغيل برنامج XMRig لعملية التعدين.
    Args:
        wallet_address (str): عنوان محفظة مونيرو.
        pool_url (str): عنوان مجمع التعدين.
        cpu_threads (int): عدد خيوط المعالج المستخدمة.
    """
    try:
        process = subprocess.Popen(
            [
                "./xmrig",  # اسم برنامج التعدين
                "--donate-level", "1",  # تحديد نسبة التبرع للمطورين
                "-o", pool_url,  # مجمع التعدين
                "-u", wallet_address,  # عنوان محفظة مونيرو
                "-p", "x",  # كلمة المرور الافتراضية
                "-t", str(cpu_threads),  # عدد الخيوط
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        return process
    except Exception as e:
        return f"Error starting miner: {e}"

def get_mining_status(process):
    """
    قراءة تقدم عملية التعدين من خلال مخرجات البرنامج.
    Args:
        process: العملية التي تم تشغيلها بواسطة XMRig.
    Returns:
        التقدم الحالي في التعدين (على شكل نص).
    """
    try:
        output = process.stdout.readline()
        if output == b"" and process.poll() is not None:
            return None
        if output:
            return output.decode("utf-8").strip()
    except Exception as e:
        return f"Error fetching status: {e}"
