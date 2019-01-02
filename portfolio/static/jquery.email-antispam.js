$(function () {
    $('a[href^="mailto:"]').each(function () {
        this.href = this.href.replace('(att)', '@').replace(/\(dott\)/g, '.');
    });
});
