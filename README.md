# Example

No test output created

# Unsolicited Opinion

Depending on the usecases of your intended audience I would advocate to simplify the CLI. Here is my unsolicited personal opinion ;)

 - perhaps group options by category, like git does?
 - maybe some options can be considered expert-options if they are used rarely?
 - perhaps most of your intended audience's usecases could be met with some merged options? (btw. I just want to start with some simple unittest-skeletons (c.f. auger, pythoscope))
 - what is the point of max-iteration if there are more than max-iterations? Even if max-iteration is not a stopping-condition and there is something else to be done I would expect max-iterations to limit iterations …
 - perhaps a per project config file ./.pynguin.ini and a per user config file like ~/.pynguin.ini or ~/.config/pynguin.ini could simplify the amount of options that have to be given via CLI? I would want to put stuff that changes rarely in these and hide those cli-options as part of the expert-help mentioned above.
 
 If the CLI interface would be simpler, there would be less confusion with user issues and also less of the documentation or a lack thereof. I think it is a little bit overwhelming. I don't want to sound ungrateful … I hope this feedback is helpful to you.
