import apache_beam as beam


class ValidateLoan(beam.DoFn):

    def process(self, record):

        try:

            if record["loan_amount"] <= 0:
                return

            if record["interest_rate"] <= 0:
                return

            yield record

        except Exception:
            pass