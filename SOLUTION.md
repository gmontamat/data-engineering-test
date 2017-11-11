# DataScience Data Engineering Test Solution

The issue in this *UTF-16LE* tab-separated file is that some of it fields contain the characters `\n`, `\r`, and `\t`
but aren't quoted. The problematic fields appear to be `first_name` and `last_name`, which could also be empty. We can
use the fact that the `account_number` field is a 5 or 6-digit number (may contain a dash or a slash in the between),
that the `email` field contains a properly formatted email address, and that the `id` field is a number between 1 and
1000. Apart from fixing problematic fields, we need to change the encoding to *UTF-8* which is more common.

### Field characteristics

* `id`: number between 1 and 1000
* `first_name`: text (contains any character, assume there are no `\t` to split from `last_name`). Could be empty.
* `last_name`: text (contains any character). Could be empty.
* `account_number`: 5 or 6 digits that may include a dash (-) or slash (/) in between
* `email`: properly formatted email address
