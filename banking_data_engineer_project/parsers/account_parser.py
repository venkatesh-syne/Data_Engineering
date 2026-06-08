import apache_beam as beam
from datetime import datetime

class ParseAccount(beam.DoFn):

    def __init__(self,batch_id):

        self.batch_id=batch_id

    def process(self,line):

        f=line.split(",")

        yield {

            "account_id": int(f[0]),
            "customer_id": int(f[1]),
            "account_type": f[2],
            "balance": float(f[3]),
            "status": f[4],
            "created_at": f[5],

            "batch_id": self.batch_id,

            "ingestion_time":
            datetime.utcnow().isoformat()
        }