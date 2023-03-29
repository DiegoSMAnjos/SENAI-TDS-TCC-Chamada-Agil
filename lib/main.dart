import 'package:flutter/material.dart';

void main() {
  runApp(CommunicationApp());
}

class CommunicationApp extends StatefulWidget {
  @override
  _CommunicationAppState createState() => _CommunicationAppState();
}

class _CommunicationAppState extends State<CommunicationApp> {
  List<String> _messages = [];

  TextEditingController _textEditingController = TextEditingController();

  void _addMessage(String message) {
    setState(() {
      _messages.add(message);
    });
  }

  void _sendMessage() {
    String message = _textEditingController.text;
    _textEditingController.clear();

    _addMessage(message);
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Communication App',
      home: Scaffold(
        appBar: AppBar(
          title: Text('Communication App'),
        ),
        body: Column(
          children: <Widget>[
            Expanded(
              child: ListView.builder(
                itemCount: _messages.length,
                itemBuilder: (context, index) {
                  return ListTile(
                    title: Text(_messages[index]),
                  );
                },
              ),
            ),
            Container(
              child: Row(
                children: <Widget>[
                  Expanded(
                    child: Padding(
                      padding: EdgeInsets.all(8.0),
                      child: TextField(
                        controller: _textEditingController,
                        decoration: InputDecoration(
                          hintText: 'Enter your message',
                        ),
                      ),
                    ),
                  ),
                  IconButton(
                    icon: Icon(Icons.send),
                    onPressed: _sendMessage,
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
