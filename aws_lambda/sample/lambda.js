exports.handler = async (event, context) => {
  const ok = Math.random() > 0.3;
  let body = ok ? { res: "ok" } : { res: "error" };
  if (Math.random() > 0.8) {
    throw "Error";
  }
  let statusCode = ok ? "200" : "500";
  const headers = {
    "Content-Type": "application/json",
  };

  return {
    statusCode,
    body: JSON.stringify(body),
    headers,
  };
};
