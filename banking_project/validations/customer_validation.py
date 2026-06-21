import apache_beam as beam


class ValidateCustomer(beam.DoFn):

    def process(self, record):

        try:

            if not record["customer_id"]:
                return

            if "@" not in record["email"]:
                return

            yield record

        except Exception:
            pass