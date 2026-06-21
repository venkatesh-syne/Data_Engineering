import apache_beam as beam


class ValidateTransaction(beam.DoFn):

    def process(self, record):

        try:

            if record["amount"] <= 0:
                return

            if record["transaction_type"] not in ["credit", "debit"]:
                return

            yield record

        except Exception:
            pass