import { APIGatewayEvent, Callback, Context, Handler } from 'aws-lambda';
import plantumlEncoder from 'plantuml-encoder';

export const encodeHandler: Handler = (event: APIGatewayEvent, context: Context, cb: Callback) => {
  const text = event.body;
  const response_text = plantumlEncoder.encode(text);
  const response = {
      "statusCode": 200,
      "body": response_text,
  };

  cb(null, response);
};
