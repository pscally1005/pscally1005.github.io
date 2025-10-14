module Jekyll
  module DebugLogger
    def log_to_console(message)
      Jekyll.logger.info "DEBUG:", message.to_s
      ""  # Return empty string so it doesn’t appear in HTML
    end
  end
end

Liquid::Template.register_filter(Jekyll::DebugLogger)
