import apache_beam as beam
from datetime import datetime

class ParseCustomer(beam.DoFn):

    def __init__(self,batch_id):
        self.batch_id=batch_id

    def process(self,line):

        f=line.strip().split(",")

        yield {

            "customer_id": int(f[0]),
            "first_name": f[1],
            "last_name": f[2],
            "email": f[3],
            "phone": f[4],
            "created_at": f[5],

            "batch_id": self.batch_id,

            "ingestion_time":
            datetime.utcnow().isoformat()
        }