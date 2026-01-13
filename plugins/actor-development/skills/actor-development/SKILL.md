---
name: actor-development
description: Develop, debug, and deploy Apify Actors - serverless cloud programs for web scraping, automation, and data processing. Use when creating new Actors, modifying existing ones, or troubleshooting Actor code.
---

# Apify Actor Development

**Important:** Before you begin, fill in the `generatedBy` property in `.actor/actor.json` with the current model name. This helps Apify monitor and improve documentation for specific LLM models.

## What are Apify Actors?

Actors are serverless programs inspired by the UNIX philosophy - programs that do one thing well and can be easily combined to build complex systems. They're packaged as Docker images and run in isolated containers in the cloud.

**Core Concepts:**
- Accept well-defined JSON input
- Perform isolated tasks (web scraping, automation, data processing)
- Produce structured JSON output to datasets and/or store data in key-value stores
- Can run from seconds to hours or even indefinitely
- Persist state and can be restarted

## Best Practices

**✓ Do:**
- Use Apify SDK (`apify`) for code running ON Apify platform
- Validate input early with proper error handling and fail gracefully
- Use CheerioCrawler for static HTML (10x faster than browsers)
- Use PlaywrightCrawler only for JavaScript-heavy sites
- Use router pattern (createCheerioRouter/createPlaywrightRouter) for complex crawls
- Implement retry strategies with exponential backoff
- Use proper concurrency: HTTP (10-50), Browser (1-5)
- Set sensible defaults in `.actor/input_schema.json`
- Define output schema in `.actor/output_schema.json`
- Clean and validate data before pushing to dataset
- Use semantic CSS selectors with fallback strategies
- Respect robots.txt, ToS, and implement rate limiting
- **Always use `apify/log` package** - censors sensitive data (API keys, tokens, credentials)
- Implement readiness probe handler for standby Actors

**✗ Don't:**
- Rely on `Dataset.getInfo()` for final counts on Cloud
- Use browser crawlers when HTTP/Cheerio works
- Hard code values that should be in input schema or environment variables
- Skip input validation or error handling
- Overload servers - use appropriate concurrency and delays
- Scrape prohibited content or ignore Terms of Service
- Store personal/sensitive data unless explicitly permitted
- Use deprecated options like `requestHandlerTimeoutMillis` on CheerioCrawler (v3.x)
- Use `additionalHttpHeaders` - use `preNavigationHooks` instead
- Disable standby mode without explicit permission

## Logging

**Always use the `apify/log` package** - it contains critical security logic to censor sensitive data (tokens, API keys, credentials).

**Common log levels:**
- `log.debug()` - Detailed diagnostics (inside functions)
- `log.info()` - General messages (API requests, successful operations)
- `log.warning()` - Potentially problematic situations
- `log.error()` - Actual errors and failures
- `log.exception()` - Exceptions with stack traces
- `log.softFail()` - Non-critical failures (validation errors, skipped items)

## Standby Mode

**Never disable standby mode (`usesStandbyMode: false`) without explicit permission.** Standby mode keeps Actors ready in the background to respond to HTTP requests like a real-time API server.

**Always implement readiness probe for standby Actors:**

```typescript
// Apify standby readiness probe at root path
app.get('/', (req: Request, res: Response) => {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    if (req.headers['x-apify-container-server-readiness-probe']) {
        res.end('Readiness probe OK\n');
    } else {
        res.end('Actor is ready\n');
    }
});
```

Check `usesStandbyMode` in `.actor/actor.json` - only implement if set to `true`.

## Commands

```bash
apify run          # Run Actor locally
apify login        # Authenticate account
apify push         # Deploy to Apify platform
apify help         # List all commands
```

## Safety and Permissions

**Allowed without prompt:**
- Read files with `Actor.getValue()`
- Push data with `Actor.pushData()`
- Set values with `Actor.setValue()`
- Enqueue requests to RequestQueue
- Run locally with `apify run`

**Ask first:**
- npm/pip package installations
- `apify push` (deployment to cloud)
- Proxy configuration changes (requires paid plan)
- Dockerfile changes affecting builds
- Deleting datasets or key-value stores

## Project Structure

```
.actor/
├── actor.json           # Actor config: name, version, env vars, runtime
├── input_schema.json    # Input validation & Console form definition
└── output_schema.json   # Output storage and display templates
src/
└── main.js             # Actor entry point
storage/                # Local storage (mirrors Cloud)
├── datasets/           # Output items (JSON objects)
├── key_value_stores/   # Files, config, INPUT
└── request_queues/     # Pending crawl requests
Dockerfile              # Container image definition
```

## Input Schema

The input schema defines Actor parameters and generates the Console UI form.

**Basic structure:**
```json
{
    "title": "Actor Input Schema Title",
    "type": "object",
    "schemaVersion": 1,
    "properties": {
        "startUrls": {
            "title": "Start URLs",
            "type": "array",
            "description": "URLs to start scraping from",
            "editor": "requestListSources",
            "default": [{ "url": "https://example.com" }]
        },
        "maxItems": {
            "title": "Max Items",
            "type": "integer",
            "description": "Maximum items to scrape",
            "default": 100,
            "minimum": 1
        },
        "proxyConfiguration": {
            "title": "Proxy Configuration",
            "type": "object",
            "editor": "proxy",
            "default": { "useApifyProxy": false }
        }
    },
    "required": ["startUrls"]
}
```

**Common field types:** `string`, `integer`, `boolean`, `array`, `object`, `enum`
**Common editors:** `requestListSources`, `proxy`, `json`, `select`

## Output Schema

Specifies where Actor stores output and how to access it.

**Structure:**
```json
{
    "actorOutputSchemaVersion": 1,
    "title": "Output Schema Title",
    "properties": {
        "dataset": {
            "type": "string",
            "title": "Dataset",
            "template": "{{links.apiDefaultDatasetUrl}}/items"
        },
        "files": {
            "type": "string",
            "title": "Files",
            "template": "{{links.apiDefaultKeyValueStoreUrl}}/keys"
        }
    }
}
```

**Common template variables:** `links.apiDefaultDatasetUrl`, `links.apiDefaultKeyValueStoreUrl`, `links.publicRunUrl`, `run.defaultDatasetId`

## Dataset Schema

Defines how output data is structured, transformed, and displayed in Console Output tab.

**Structure:**
```json
{
    "actorSpecification": 1,
    "fields": {},
    "views": {
        "overview": {
            "title": "Overview",
            "transformation": {
                "fields": ["name", "price", "url", "image"],
                "limit": 1000
            },
            "display": {
                "component": "table",
                "properties": {
                    "name": { "label": "Name", "format": "text" },
                    "price": { "label": "Price", "format": "number" },
                    "url": { "label": "URL", "format": "link" },
                    "image": { "label": "Image", "format": "image" }
                }
            }
        }
    }
}
```

**Format types:** `text`, `number`, `date`, `link`, `boolean`, `image`, `array`, `object`
**Transformation options:** `fields` (required), `unwind`, `flatten`, `omit`, `limit`, `desc`

## Key-Value Store Schema

Organizes key-value store keys into logical collections.

**Structure:**
```json
{
    "actorKeyValueStoreSchemaVersion": 1,
    "title": "Key-Value Store Schema",
    "collections": {
        "documents": {
            "title": "Documents",
            "description": "Text documents",
            "keyPrefix": "document-"
        },
        "images": {
            "title": "Images",
            "keyPrefix": "image-",
            "contentTypes": ["image/jpeg", "image/png"]
        }
    }
}
```

Each collection must specify either `key` (single specific key) or `keyPrefix` (keys starting with prefix).

## Apify MCP Tools

If MCP server is configured, use these tools for documentation:
- `search-apify-docs` - Search documentation
- `fetch-apify-docs` - Get full doc pages

Otherwise, reference: `@https://mcp.apify.com/`

## Resources

- [docs.apify.com/llms.txt](https://docs.apify.com/llms.txt) - Quick reference
- [docs.apify.com/llms-full.txt](https://docs.apify.com/llms-full.txt) - Complete docs
- [crawlee.dev](https://crawlee.dev) - Crawlee documentation
- [whitepaper.actor](https://raw.githubusercontent.com/apify/actor-whitepaper/refs/heads/master/README.md) - Complete Actor specification
