import apache_beam as beam
from datetime import datetime

class ParseCard(beam.DoFn):

    def __init__(self,batch_id):
        self.batch_id=batch_id

    def process(self,line):

        f=line.strip().split(",")

        yield {

            "card_id": int(f[0]),
            "customer_id": int(f[1]),
            "card_type": f[2],
            "card_limit": float(f[3]),
            "issued_date": f[4],

            "batch_id": self.batch_id,

            "ingestion_time":
            datetime.utcnow().isoformat()
        }