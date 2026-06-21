import apache_beam as beam
from datetime import datetime

class ParseLoan(beam.DoFn):

    def __init__(self,batch_id):
        self.batch_id=batch_id

    def process(self,line):

        f=line.strip().split(",")

        yield {

            "loan_id": int(f[0]),
            "customer_id": int(f[1]),
            "loan_amount": float(f[2]),
            "interest_rate": float(f[3]),
            "loan_status": f[4],
            "created_at": f[5],

            "batch_id": self.batch_id,

            "ingestion_time":
            datetime.utcnow().isoformat()
        }