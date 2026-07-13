#!/bin/bash

# curl-test.sh
# Tests the POST, GET, and DELETE /api/timeline_post endpoints

BASE_URL="http://127.0.0.1:5000/api/timeline_post"

echo "=== Creating a random timeline post ==="

RANDOM_NAME="TestUser$RANDOM"
RANDOM_CONTENT="This is a test post created at $(date) with random id $RANDOM"

POST_RESPONSE=$(curl -s -X POST "$BASE_URL" \
  -H "Content-Type: application/json" \
  -d "{\"name\": \"$RANDOM_NAME\", \"email\": \"$RANDOM_NAME@example.com\", \"content\": \"$RANDOM_CONTENT\"}")

echo "POST response:"
echo "$POST_RESPONSE"

# Extract the id of the newly created post using basic text parsing
POST_ID=$(echo "$POST_RESPONSE" | grep -o '"id": *[0-9]*' | grep -o '[0-9]*')

if [ -z "$POST_ID" ]; then
  echo "FAILED: Could not extract post ID from response. Aborting."
  exit 1
fi

echo "Created post with ID: $POST_ID"

echo ""
echo "=== Fetching all timeline posts ==="
GET_RESPONSE=$(curl -s "$BASE_URL")
echo "$GET_RESPONSE"

# Check if our new post's content appears in the GET response
if echo "$GET_RESPONSE" | grep -q "$RANDOM_CONTENT"; then
  echo ""
  echo "SUCCESS: New post found in GET response."
else
  echo ""
  echo "FAILED: New post NOT found in GET response."
  exit 1
fi

echo ""
echo "=== Deleting the test post (ID: $POST_ID) ==="
DELETE_RESPONSE=$(curl -s -X DELETE "$BASE_URL/$POST_ID")
echo "$DELETE_RESPONSE"

echo ""
echo "=== Confirming post was deleted ==="
GET_RESPONSE_AFTER=$(curl -s "$BASE_URL")
echo "$GET_RESPONSE_AFTER"

if echo "$GET_RESPONSE_AFTER" | grep -q "$RANDOM_CONTENT"; then
  echo ""
  echo "FAILED: Post still exists after DELETE."
  exit 1
else
  echo ""
  echo "SUCCESS: Post successfully deleted."
fi
