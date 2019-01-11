# movie_notifier

## lambda deploy
```sh
# create zip
zip -r movie_notifier.zip *

# upload lambda
aws lambda update-function-code \
--profile <profile_name> \
--function-name <function_name> \
--zip-file fileb://<file_path> \
--publish
```
