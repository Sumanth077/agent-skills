# Apify Agent Skills

Official Apify agent skills for web scraping, data extraction, and automation. Works with Claude Code, Cursor, Codex, Gemini CLI, and other AI coding assistants.

## Available Skills

<!-- BEGIN_SKILLS_TABLE -->
| Name | Description | Documentation |
|------|-------------|---------------|
| `lead-generation` | Generate B2B/B2C leads by scraping Google Maps, websites, Instagram, TikTok, Facebook, LinkedIn, YouTube, and Google Search using Apify Actors | [SKILL.md](skills/lead-generation/SKILL.md) |
<!-- END_SKILLS_TABLE -->

## Installation

### Claude Code

```bash
# Add the marketplace
/plugin marketplace add https://github.com/apify/agent-skills

# Install a skill
/plugin install lead-generation@apify-agent-skills
```

### Cursor / Windsurf

Add to your project's `.cursor/settings.json` or use the same Claude Code plugin format.

### Codex / Gemini CLI

Point your agent to the `agents/AGENTS.md` file which contains skill descriptions and paths:

```bash
# Gemini CLI uses gemini-extension.json automatically
# For Codex, reference agents/AGENTS.md in your configuration
```

### Other AI Tools

Any AI tool that supports markdown context can use the skills by pointing to:
- `agents/AGENTS.md` - Auto-generated skill index
- `skills/*/SKILL.md` - Individual skill documentation

## Prerequisites

1. **Apify Account**: Sign up at [apify.com](https://apify.com)
2. **API Token**: Get your token from [Apify Console > Integrations](https://console.apify.com/account/integrations)
3. **Set Environment Variable**: Add to your `.env` file:
   ```
   APIFY_TOKEN=your_token_here
   ```

## Output Formats

- **Quick Answer** - Top 5 results displayed in chat (default, no file saved)
- **CSV** - Full export or basic fields only
- **JSON** - Full data export

## Pricing

Apify Actors use pay-per-result pricing. Check individual Actor pricing on [apify.com](https://apify.com).

## Contributing

1. Fork this repository
2. Create your skill in `skills/your-skill-name/`
3. Add `SKILL.md` with proper frontmatter:
   ```yaml
   ---
   name: your-skill-name
   description: What your skill does and when to use it
   ---
   ```
4. Add entry to `.claude-plugin/marketplace.json`
5. Run `uv run scripts/generate_agents.py` to update AGENTS.md
6. Submit a pull request

## Development

```bash
# Regenerate AGENTS.md and validate marketplace.json
uv run scripts/generate_agents.py
```

## Future Skills

### Outcome-based
- `brand-monitoring` - Review tracking, sentiment analysis
- `competitor-intelligence` - Benchmarking, feature comparison
- `influencer-discovery` - Find and vet influencers
- `trend-analysis` - Hashtag tracking, viral content

### Platform-based
- `google-intelligence` - Maps, Search, Trends, Booking
- `instagram-intelligence` - Profiles, Posts, Reels, Hashtags
- `facebook-intelligence` - Pages, Posts, Groups, Ads
- `tiktok-intelligence` - Profiles, Videos, Hashtags, Sounds
- `youtube-intelligence` - Channels, Videos, Shorts, Comments

## Support

- [Apify Documentation](https://docs.apify.com)
- [Apify Discord](https://discord.gg/jyEM2PRvMU)
