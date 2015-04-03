import logging
import os
import six

from bzt.utils import MultiPartForm
from tests import BZTestCase, __dir__


class TestMultiPartForm(BZTestCase):
    def test___init__(self):
        body = MultiPartForm()

        additional_files = os.listdir(__dir__() + "/data")

        for extra_file in additional_files:
            extra_file = __dir__() + six.u("/data/") + extra_file
            with open(os.path.expanduser(extra_file), 'rb') as fd:
                file_data = fd.read()

            fname = os.path.basename(extra_file)
            encoded = six.u("file_%s") % extra_file
            body.add_file_as_string(encoded, fname, file_data)

        txt = body.form_as_bytes()
        logging.debug("%s", len(txt))