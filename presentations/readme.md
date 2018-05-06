# Presentation tools

You can use Golang's presentation tool to construct slides.

## Run present tool

In the folder containing the `.slide` file, run the `present` command to start a webserver with your presentation.

Access at `localhost:3999`

## `.slide` files

```
Title of document
Subtitle of document
15:04 2 Jan 2006
Tags: foo, bar, baz

Author Name
Job title, Company
joe@example.com
http://url/
@twitter_name
Some Text

* Title of slide or section (must have asterisk)

Some Text
```

## Install presentation tool

`go install golang.org/x/tools/cmd/present`

You can run the present tool with the `present` command or from your $GOPATH: `$GOPATH/bin/present`

## Further reading:

- [Go presentation tool](http://halyph.com/blog/2015/05/18/golang-presentation-tool.html)
- [Dave Cheney's presentations](https://github.com/davecheney/presentations)
