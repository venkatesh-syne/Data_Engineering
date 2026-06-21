import apache_beam as beam
from datetime import datetime

class ParseTransaction(beam.DoFn):

    def __init__(self,batch_id):
        self.batch_id=batch_id

    def process(self,line):

        f=line.strip().split(",")

        yield {

            "transaction_id": int(f[0]),
            "account_id": int(f[1]),
            "transaction_type": f[2],
            "amount": float(f[3]),
            "transaction_time": f[4],
            "description": f[5],

            "batch_id": self.batch_id,

            "ingestion_time":
            datetime.utcnow().isoformat()
        }